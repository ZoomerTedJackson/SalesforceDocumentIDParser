
<div align="center">
<h3 align="center">Salesforce Document ID Parser</h3>
  <p align="center">
    A short script that parses the JSON output when dumping Document IDs from a Salesforce CDN
    <br />
  </p>
</div>
<h2>About</h2>
I wrote this up quickly to convert the JSON output you get when dumping document IDs from a Salesforce CDN into an easy file.
 <br /> <br />
This should be able to create the list of IDs from the output of "entityNameOrId":"ContentVersion" & "entityNameOrId":"ContentDocument"

<h2>Usage</h2>
Simply run this and in the command line arguments add the JSON file. It will output the list of IDs in a file called "Salesforce_Document_IDs.txt". This expects the output to look the same as from the above example from Clark Voss, and i made this quickly for one use, so no promises it works.

```
python ./main.py /path/to/file.json
```
