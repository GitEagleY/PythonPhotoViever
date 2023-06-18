<p align="center">
  <h1 align="center">PythonPhotoViever</h1>
</p>

# Prerequisites

Before running the application, make sure you have the following installed:

   - [Python 3](https://www.python.org/downloads/) (version 3.6 or above)
   - tkinter library
   - PIL module (you can install it using pip install Pillow)

# Usage

To run the application, follow these steps:

   - Clone or download the repository to your local machine.

   - Open a terminal or command prompt and navigate to the project directory.

   - Run the following command:

    python main.py

The photo viewer application will launch.

# Building

To build the photo viewer app into an executable file, follow these steps:

  1. Make sure you have PyInstaller installed by running pip install pyinstaller in your terminal.

  2. Navigate to the project directory where the cloned photo viewer app is located.

  3. Run the command  
         
         pyinstaller --onefile main.py 
    
   in the terminal to create a standalone executable.

   4. After the process completes, you'll find a dist directory in your project folder.

   5. Inside the dist directory, you'll find the generated executable file named photo_viewer.exe (for Windows) or photo_viewer (for Linux).

   6. Optionally, ensure the executable file has executable permissions on Linux by running 
          
          chmod +x <executable file name> 
          
   in the terminal.

## License

This project is licensed under the The GNU General Public License (GPL) License.
