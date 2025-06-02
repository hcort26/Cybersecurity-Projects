# MicrosoftGUI - GitHub Repository Creator (Prototype)

This application provides a graphical way to convert a local project into a Git repository and automatically push it to GitHub.

## Features

- Initialize a Git repository from a local project.
- Create a `.gitignore` file with common patterns.
- Create a `README.md` file containing the project name.
- Create a remote GitHub repository using the GitHub API.
- Set the remote `origin` and push the initial commit.
- Return the GitHub URL of the created repository.
- Display a prototype disclaimer in the GUI.

## Requirements

- Java 17 or higher
- Visual Studio Code (recommended) or any compatible Java IDE
- Git installed locally
- A GitHub account
- A GitHub Personal Access Token (PAT)

## External Libraries

This project requires two external Java libraries:

| GitSubprocessClient | Allows running Git commands from Java |
| GitHubApiClient | Enables communication with GitHub API from Java |

Both libraries should be manually downloaded and placed inside the `/libs` folder. They should be added to the project's referenced libraries in the IDE.

## Setup Instructions

1. **Clone the Repository**  
   Clone the project repository to your local machine.

2. **Download Required Libraries**  
   Download the `GitSubprocessClient` and `GitHubApiClient` JAR files and place them inside the `/libs` directory.

3. **Add External Libraries to Project**  
   - Open the project in Visual Studio Code.
   - Open the Java Projects sidebar.
   - Under "Referenced Libraries," click the "+" icon and add both JAR files from the `/libs` folder.

4. **Run the Application**  
   You can launch the application directly from Visual Studio Code using the Play button

## Usage Notes

- You will need to supply a valid GitHub Personal Access Token to authenticate API requests.
- Do not commit any sensitive information such as Personal Access Tokens to GitHub.
- If using this project for local testing, replace your token with a placeholder before pushing to a remote repository.

## Security Notice

This application requires the use of a GitHub Personal Access Token.  
Personal Access Tokens must never be committed to any repository or shared publicly.  
Always replace real tokens with placeholders when sharing code.

## Prototype Disclaimer

This application is a prototype created for academic purposes and is not intended for production or commercial deployment. Functionality may be limited and subject to change.

## Project Contributors

- Henry
- Shane
- Phil
