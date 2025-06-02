import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GitRepoCreatorGUI extends JFrame {

    private JTextField projectPathField;
    private JTextField usernameField;
    private JPasswordField tokenField;
    private JTextField repoNameField;
    private JLabel statusLabel;

    public GitRepoCreatorGUI() {
        setTitle("GitHub Repo Creator");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(500, 440);
        setLocationRelativeTo(null);

        initComponents();
    }

    private void initComponents() {
        JPanel mainPanel = new JPanel(new BorderLayout());
        JPanel formPanel = new JPanel(new GridLayout(6, 2, 10, 10));
        formPanel.setBorder(BorderFactory.createEmptyBorder(10, 20, 10, 20));

        // Logo
        JLabel logoLabel = new JLabel();
        ImageIcon logoIcon = new ImageIcon("ProjectLogo.png"); 
        logoLabel.setIcon(new ImageIcon(logoIcon.getImage().getScaledInstance(120, 120, Image.SCALE_SMOOTH)));
        logoLabel.setHorizontalAlignment(JLabel.CENTER);
        mainPanel.add(logoLabel, BorderLayout.NORTH);

        // Form fields
        JLabel projectPathLabel = new JLabel("Local Project Path:");
        projectPathField = new JTextField();

        JLabel usernameLabel = new JLabel("GitHub Username:");
        usernameField = new JTextField();

        JLabel tokenLabel = new JLabel("GitHub Token:");
        tokenField = new JPasswordField();

        JLabel repoNameLabel = new JLabel("Repository Name:");
        repoNameField = new JTextField();

        JButton createButton = new JButton("Create Repository");
        createButton.addActionListener(new CreateRepoListener());

        statusLabel = new JLabel(" ");
        statusLabel.setForeground(Color.BLUE);

        formPanel.add(projectPathLabel);
        formPanel.add(projectPathField);

        formPanel.add(usernameLabel);
        formPanel.add(usernameField);

        formPanel.add(tokenLabel);
        formPanel.add(tokenField);

        formPanel.add(repoNameLabel);
        formPanel.add(repoNameField);

        formPanel.add(createButton);
        formPanel.add(statusLabel);

        mainPanel.add(formPanel, BorderLayout.CENTER);

        // Disclaimer
        JLabel disclaimer = new JLabel("This application is a prototype and not intended for commercial use.");
        disclaimer.setHorizontalAlignment(JLabel.CENTER);
        disclaimer.setFont(new Font("Arial", Font.ITALIC, 11));
        disclaimer.setForeground(Color.DARK_GRAY);
        disclaimer.setBorder(BorderFactory.createEmptyBorder(5, 0, 10, 0));
        mainPanel.add(disclaimer, BorderLayout.SOUTH);

        add(mainPanel);
    }

    private class CreateRepoListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            String projectPath = projectPathField.getText().trim();
            String username = usernameField.getText().trim();
            String token = new String(tokenField.getPassword()).trim();
            String repoName = repoNameField.getText().trim();

            if (projectPath.isEmpty() || username.isEmpty() || token.isEmpty() || repoName.isEmpty()) {
                statusLabel.setText("❗ All fields are required.");
                return;
            }

            GitRepoCreator creator = new GitRepoCreator(username, token);
            String remoteUrl = creator.createRepo(repoName, "Repo created by GUI", false);

            if (remoteUrl == null) {
                statusLabel.setText("❌ GitHub repo creation failed.");
                return;
            }

            GitProjectInitializer initializer = new GitProjectInitializer(projectPath);
            initializer.initializeProject(repoName, remoteUrl);

            statusLabel.setText("✅ Repo created and pushed!");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            GitRepoCreatorGUI gui = new GitRepoCreatorGUI();
            gui.setVisible(true);
        });
    }
}
