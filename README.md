# myGPT
```bash
  ______________________________________
| Welcome to myGPT! What's in your mind? |
  ======================================
                                       \
                                        \
                                         \
                                          |\_/|,,_____,~~`
                                          (.".)~~     )`~}}
                                           \o/\ /---~\\ ~}}
                                             _//    _// ~}
```

# Installation

## Requirements
- OpenAI API: Please set your OpenAI API key in your environment variables. It can be set for the current session or made persistent across sessions by defining them in shell configuration files (~/.bashrc, ~/.zshrc, etc.). For example, in your `.bashrc` or `.zshrc`, add this line:
  ```bash
  export OPENAI_API_KEY=YOUR_API_KEY
  ```
- Python packages: pillow, openai, cowsay
- (optional) Render output Markdown on terminal: mdcat

# How to Use
```bash
python mygpt.py -h
```

## Assistant Mode
The Assistant mode in myGPT allows you to create or load an assistant, choose a model (such as GPT-3 or GPT-4), provide an instruction for the assistant's role, and upload files. 

When creating your assistant, you can upload files that will help the assistant answer your questions more effectively. The assistant will then provide responses based on the information provided in the uploaded files.

To get started, run the following command and follow the instructions:
```bash
python mygpt.py -m assistant
```

Output will be saved in a markdown file locally.

## Chat Mode
Start chatting with the following command:
```bash
python mygpt.py -m chat
```

# Roadmap
