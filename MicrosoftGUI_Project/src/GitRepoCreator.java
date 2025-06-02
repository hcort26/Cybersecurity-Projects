import github.tools.client.GitHubApiClient;
import github.tools.client.RequestParams;

public class GitRepoCreator {
    private GitHubApiClient client;
    private String githubUsername;

    public GitRepoCreator(String githubUsername, String githubToken) {
        this.githubUsername = githubUsername;
        this.client = new GitHubApiClient(githubUsername, githubToken);
    }

    public String createRepo(String repoName, String description, boolean isPrivate) {
        RequestParams params = new RequestParams();
        params.addParam("name", repoName);
        params.addParam("description", description);
        params.addParam("private", String.valueOf(isPrivate));

        try {
            client.createRepo(params);
            System.out.println("✅ GitHub repo created successfully!");
            return "https://github.com/" + githubUsername + "/" + repoName;
        } catch (Exception e) {
            System.out.println("❌ Failed to create GitHub repository.");
            e.printStackTrace();
            return null;
        }
    }
}

