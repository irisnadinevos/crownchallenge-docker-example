![Picture1](https://github.com/irisnadinevos/crownchallenge/assets/125289748/6ca45089-ef27-4277-96ee-4ba884f9dbe8)

##The Circle of Willis Intracranial Artery Classification and Quantification (CROWN) Challenge: http://crown.isi.uu.nl/

Example docker containers for the CROWN Challenge. The example python script can be used to see how applications can be containerized and run within the challenge.

###Python example

The python script in src/run.py creates two random classes (anterior and posterior) as output for the Lippert classification task.

This code needs a basic Python installation, with SimpleITK added.

Our Dockerfile looks like this:

'''
FROM python:3.9

RUN pip install SimpleITK ADD src/crown_example
'''
