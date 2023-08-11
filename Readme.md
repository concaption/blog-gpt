# BlogGPT
This project contains a .env file with an OPENAI_API_KEY property. This key is used to authenticate with the OpenAI API and should be kept secret.

![BlogGPT](assets/sc.png)

## Installation

1. Clone the repository
2. Install the required packages by running the following command in your terminal:

```bash
make install
```

This will install all the required packages listed in the `requirements.txt` file.

## Running the Application

To run the application, use the following command:

```bash
make run
```

This will start the application and open it in your default web browser. If it doesn't open automatically, you can navigate to `http://localhost:8501` in your web browser to view the application.

Note: Make sure to set the `OPENAI_API_KEY` environment variable before running the application. You can do this by creating a `.env` file in the root directory of the project and adding the following line:

```
OPENAI_API_KEY=<your_api_key_here>
```

Replace `<your_api_key_here>` with your actual OpenAI API key.

Contributing
Contributions are welcome! Please open an issue or pull request if you have any suggestions or improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.