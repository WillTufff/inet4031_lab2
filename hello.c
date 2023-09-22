#include <stdio.h>
int main()
{
  char arr[3][10] = {"User1",
                     "User2", "User3"};
   
  for (int i = 0; i < 3; i++)
  {
    printf("%s\n", arr[i]);
  }
  return 0;
}
