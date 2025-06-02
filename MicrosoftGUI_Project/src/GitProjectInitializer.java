import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import git.tools.client.GitSubprocessClient;


public class GitProjectInitializer {
    private GitSubprocessClient gitClient;
    private String repoPath; 

    public GitProjectInitializer(String repoPath) {
        this.repoPath = repoPath;
        this.gitClient = new GitSubprocessClient(repoPath);
    }

    public void initializeProject(String repoName, String remoteUrl) {
        try {
            // 1. Initialize Git repo
            System.out.println(gitClient.gitInit());

            // 2. Create .gitignore
            createGitIgnore();

            // 3. Create README.md
            createReadMe(repoName);

            // 4. Stage all files
            System.out.println(gitClient.gitAddAll());

            // 5. Create initial commit
            System.out.println(gitClient.gitCommit("Initial commit"));

            // 6. Add remote origin
            System.out.println(gitClient.gitRemoteAdd("origin", remoteUrl));

            // 7. Push to remote
            System.out.println(gitClient.gitPush("main"));

            System.out.println("Project initialized and pushed successfully!");

        } catch (Exception e) {
            System.out.println("Something went wrong during Git initialization: " + e.getMessage());
        }
    }

    private void createGitIgnore() throws IOException {
        File gitignore = new File(repoPath + "/.gitignore");
        try (FileWriter writer = new FileWriter(gitignore)) {
            writer.write(".DS_Store\n");
            writer.write("*.class\n");
            writer.write("*.log\n");
            writer.write("*.jar\n");
            writer.write("target/\n");
            writer.write(".idea/\n");
            writer.write(".vscode/\n");
            writer.write("*.iml\n");
        }
    }
    
    private void createReadMe(String projectName) throws IOException {
        File readme = new File(repoPath + "/README.md");
        try (FileWriter writer = new FileWriter(readme)) {
            writer.write("# " + projectName + "\n");
            writer.write("\nThis is an auto-generated README file.");
        }
    }
}

