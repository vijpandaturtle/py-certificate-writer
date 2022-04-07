# Certificate Writer
A simple python script to populate course/webinar certificates with personal details

## Installation 
1. Get the dependencies 
```
pip install pandas PyPDF2 reportlab
```
2. You need to have a CSV file with the details. Currently this script accepts a CSV file with two columns ['Name', 'Institution']
3. Modify the csv_file_path and original_certificate_path variables
4. Run the script
```
python certificate.py
```
And that's it ! 