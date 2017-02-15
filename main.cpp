#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string>

std::string category = "argos";

class TLE{
  private:
    int value, category, satNr;

  public:
    void get_data(int, int, int);
    void download();
};

void TLE::get_data(int value, int category, int satNr){
  std::string line;

  // open file
  std::ifstream file ("TLE/argos.txt");

  // run if file is open
  if(file.is_open()){

    // cycle to specific TLE
    for(int i = 1; i <= ((3 * satNr)-3); i++){
        std::getline(file, line);
    }

    if(value == 1){
      std::getline(file, line);
      for(int i = 0; i < 24; i++){
        std::cout << line[i];
      }
    }

    else if(value == 2){
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 0; i < 1; i++){
        std::cout << line[i];
      }
    }

    else if(value == 3){
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 7; i < 8; i++){
        std::cout << line[i];
      }
    }

    else if(value == 4){
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 9; i < 11; i++){
        std::cout << line[i];
      }
    }

    else if(value == 5){
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 11; i < 14; i++){
        std::cout << line[i];
      }
    }

    else if(value == 6){
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 14; i < 17; i++){
        std::cout << line[i];
      }
    }

    else if(value == 7){
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 18; i < 20; i++){
        std::cout << line[i];
      }
    }

    else if(value == 8){
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 20; i < 32; i++){
        std::cout << line[i];
      }
    }

    else if(value == 9){
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 20; i < 23; i++){
        std::cout << line[i];
      }
    }

    else if(value == 10){
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 24; i < 32; i++){
        std::cout << line[i];
      }
    }

    else if(value == 11){
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 33; i < 43; i++){
        std::cout << line[i];
      }
    }

    else if(value == 12){
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 44; i < 52; i++){
        std::cout << line[i];
      }
    }

    else if(value == 13){
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 53; i < 61; i++){
        std::cout << line[i];
      }
    }

    else if(value == 14){
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 62; i < 63; i++){
        std::cout << line[i];
      }
    }

    else if(value == 15){
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 64; i < 68; i++){
        std::cout << line[i];
      }
    }

    else if(value == 16){
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 68; i < 69; i++){
        std::cout << line[i];
      }
    }

    else if(value == 17){
      std::getline(file, line);
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 0; i < 1; i++){
        std::cout << line[i];
      }
    }

    else if(value == 18){
      std::getline(file, line);
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 2; i < 7; i++){
        std::cout << line[i];
      }
    }

    else if(value == 19){
      std::getline(file, line);
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 8; i < 16; i++){
        std::cout << line[i];
      }
    }

    else if(value == 20){
      std::getline(file, line);
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 17; i < 25; i++){
        std::cout << line[i];
      }
    }

    else if(value == 21){
      std::getline(file, line);
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 26; i < 33; i++){
        std::cout << line[i];
      }
    }

    else if(value == 22){
      std::getline(file, line);
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 34; i < 42; i++){
        std::cout << line[i];
      }
    }

    else if(value == 23){
      std::getline(file, line);
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 42; i < 51; i++){
        std::cout << line[i];
      }
    }

    else if(value == 24){
      std::getline(file, line);
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 52; i < 63; i++){
        std::cout << line[i];
      }
    }

    else if(value == 25){
      std::getline(file, line);
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 63; i < 68; i++){
        std::cout << line[i];
      }
    }

    else if(value == 26){
      std::getline(file, line);
      std::getline(file, line);
      std::getline(file, line);
      for(int i = 68; i < 69; i++){
        std::cout << line[i];
      }
    }

    // std::getline(file, line);
    // std::cout << line << std::endl;
    // std::getline(file, line);
    // std::cout << line << std::endl;

    file.close();
  }
  else{
    std::cout << "Unable to open file";
  }

  // std::cout << linecount << std::endl;
}

void TLE::download(){
  std::cout << category;
}


int main(){
  // system("ls -l");
  // system("python3 download_data.py");

  TLE sat;
  // sat.download();
  sat.get_data(19, 1, 2);
  std::cout << std::endl;

  return 0;
}
