FROM ubuntu:18.04

#install python and unixodbc
RUN apt-get update -y && \      
    apt-get install -y \    
    libpq-dev \    
    gcc \
    python3-pip 

    
#set locales
RUN apt-get update && apt-get install -y locales
RUN locale-gen pt_BR.UTF-8  
ENV LANG pt_BR.UTF-8  
ENV LANGUAGE pt_BR:pt  
ENV LC_ALL pt_BR.UTF-8 


COPY . /app

# install all libraries
COPY src/requirements.txt requirements.txt

RUN pip3 install --upgrade pip && pip3 install --no-cache -r /requirements.txt

# Run app
WORKDIR /app

EXPOSE 8501

# start program
ENTRYPOINT [ "streamlit","run"] 
CMD ["main.py"]
