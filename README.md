
# Self-Hosted LangSmith Setup

This repository provides an easy way to self-host LangSmith using Docker. Follow the steps below to set up and run LangSmith on your own server.

## Prerequisites
- **Docker** installed on your system  
- **Make** installed (for running the Makefile)  
- **PowerShell (Windows only)** or **Bash (Linux/Mac)**  

## Installation Steps

### 1. Clone the Repository
```sh
git clone https://github.com/SwAt1563/langfuse-setup.git
cd langfuse-setup
```

### 2. Create the Network  
Before running the container, you need to create a Docker network.  

#### **On Windows (PowerShell)**
```powershell
./create_network.ps1
```

#### **On Linux/Mac (Bash)**
```sh
./create_network.sh
```

### 3. Run LangSmith  
Once the network is created, start LangSmith using:
```sh
make run
```

This will pull and run the necessary Docker containers for LangSmith.

## Usage  
After the setup is complete, LangSmith should be running on your local server. You can access it by navigating to:  
```
http://localhost:4000
```

## Troubleshooting  
- Ensure Docker is running before executing the commands.  
- If `make run` fails, try running:
  ```sh
  docker-compose -f docker-compose.yml up 
  ```

## Contributing  
Feel free to submit issues or contribute improvements via pull requests.

## License  
This project is licensed under MIT License. 
