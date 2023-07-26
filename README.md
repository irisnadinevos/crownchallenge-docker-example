## The Circle of Willis Intracranial Artery Classification and Quantification (CROWN) Challenge
http://crown.isi.uu.nl/

Example docker containers for the CROWN Challenge. The example python script can be used to see how applications can be containerized and run within the challenge.

### Python example

The [python script](https://github.com/irisnadinevos/crownchallenge/blob/main/src/run.py) in src/run.py creates two random classes (anterior and posterior) as output for the Lippert classification task.

This code needs a basic Python installation, with SimpleITK added.

Our Dockerfile looks like this:

```
FROM python:3.9

RUN pip install SimpleITK
ADD src /crown_example/
```

Note: The COPY, ADD and RUN statements add a new layer to your image. Try to combine commands into a single RUN statement; separate this only if it is required for readability.
Our Python code is saved next to this Dockerfile in the folder src/run.py. With the following command, we build a Docker container from our Dockerfile and the Python source code:

```
docker build -f Dockerfile -t crownchallenge/[TEAM-NAME]_task1 .
```

Note: the . at the end specifies that everything is in the current folder. Hence, you run this build command from the folder that contains the Dockerfile and the source code.
Once your container is ready, we can run it with the following command:

```
docker run -dit --network none -v [TEST-INPUT]:/input:ro -v /output crownchallenge/[TEAM-NAME]_task1
```

The -v options map the input folder into the container at /input, read-only. The last -v creates an output directory.
This command outputs the Container ID, which you can also look up with:

```
docker ps
```

Next, we will execute the example Python script:

```
docker exec [CONTAINER-ID] python /crown_example/run.py
```

Then we copy the output from the container to our local machine:

```
docker cp [CONTAINER-ID]:/output [RESULT-LOCATION]
```

Finally, we shut down the running container. This also removes the created /output folder and any other changes made to the container:

```
docker rm -v [CONTAINER-ID]
```

