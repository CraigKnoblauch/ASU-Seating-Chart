# ASU Seating Chart Generator
## Austin-Bren-2017F-83238
Hello professor. 

Per your request, this program will take a csv file as input, distribute students into Neeb hall while maximizing in-row distance between students. The program will create a pool of students to be seated and seat them until there are less students in the pool than rows in the hall. When this case is reached, one student is placed in each row, starting at the first row, until the student pool is empty. This means that The front rows will have one more student than the back rows. 
Also, as you requested, no students are assigned to row A. 

### Using the program
The program takes a csv file as input from a command line argument. For example, you would run this program and give it input by entering this command into your terminal.
```
python3 main.py input.csv
```
The csv file you use as input should have three **label-less** columns, that contain first names, last names, and PINs respectively. 
For example, if your input file had 35 students, cells A1:A35 would have all first names, cells B1:B35 would have all last names, and cells C1:C35 should have all PINs. 
### The output
The output file is named "seat_chart_output.csv" and will be located in the output directory. I formatted it the same as the pdf's you've released in the past. The students are sorted based on their PIN.
### Closing Remarks
The code I've included can be found on this [program's github](https://github.com/CraigKnoblauch/ASU-Seating-Chart). Specifically this code belongs to your branch:[`Austin-Bren-2017F-83238`](https://github.com/CraigKnoblauch/ASU-Seating-Chart/tree/Austin-Bren-2017F-83238). If you would like to share this resource with colleagues, please point them to this [repo](https://github.com/CraigKnoblauch/ASU-Seating-Chart). They can submit an issue to request a lecture hall, request additional features, or report bugs.
