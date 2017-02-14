#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string>

int main(){
  // system("ls -l");
  // system("python3 download_data.py");

  std::string line;
  std::ifstream file ("TLE/argos.txt");

  if(file.is_open()){
    while(getline(file, line)){
      std::cout << line << '\n';
    }
    file.close();
  }

  else{
    std::cout << "Unable to open file";
  }

  return 0;
}
