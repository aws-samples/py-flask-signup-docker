FROM jenkinsci/jnlp-slave
MAINTAINER Daniele Stroppa (stroppad@amazon.com)

# Install Selenium and PhantomJS
USER root

# Quiet the update and install output
RUN apt-get update -qq && \
    apt-get install -y -qq python-pip nodejs npm

RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN pip install selenium
RUN npm install phantom phantomjs -g

USER jenkins

COPY test_application.py /home/jenkins/
