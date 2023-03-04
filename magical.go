package main

import "fmt" // means that programmer has imported the format library which contains all the important format statements

func main() { // main function is the entry-point of the code and whenever, we run the program, it will look for the main function 

	var magicnum int 
	var magichar string
	fmt.Println("Want to play a simple even odd game??")
	fmt.Println("Let's rock and roll!!")
	fmt.Println("Enter the magical number: ")
	fmt.Scan(&magicnum)

	if (magicnum%2 == 0) {
		  magichar = "E"
          fmt.Println(magichar)
	} else {
		magichar = "0"
		fmt.Println(magichar)
	}

	fmt.Println("Here, E means you typed a even magical number and O means an odd one!!")
} // That's it phewwwww
