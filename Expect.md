Expect script – Read / write file
Thanks to this source : http://wiki.tcl.tk/367

To read data from a file in an Expect script:
```
#!/usr/bin/expect -f
 
set fd "input.txt"
set fp [open "$fd" r]
set data [read $fp]

# Read line by line

foreach line $data { 
puts "$line\r" 
}
```
# And to write data to a file:
```
#!/usr/bin/expect -f
 
set outputFilename "output.txt"
set outFileId [open $outputFilename "w"]
 
puts -nonewline $outFileId "A first line\n"
puts -nonewline $outFileId "A second line\n"
 
#Close file descriptor to ensure data are flush to file
close $outFileId
```
