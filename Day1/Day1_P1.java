/*
Author: Rocky Mazorow
Date: 12/9/2019

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
*/

import java.util.Scanner;
import java.io.*;

class Day1_P1 {
	public static void main(String[] args) {
		try {
			Scanner input = new Scanner(new File("Day1.txt"));
			int sum = 0;
			int mass = 0;
			
			while (input.hasNext()) {
				mass = input.nextInt();
				sum += (mass / 3 - 2);
			}
			
			System.out.println("The sum of all modules is: " + sum);
			input.close();
		}
		catch (FileNotFoundException e) {
			System.out.println("File not found");
		}
	}
}