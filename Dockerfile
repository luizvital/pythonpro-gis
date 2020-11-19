FROM jupyter/minimal-notebook

ENV GRANT_SUDO=yes
USER root

RUN sudo -u root apt-get update && sudo -u root apt-get install -qq -y \
    libgdal20 libpq-dev libgeos-c1v5 --no-install-recommends

USER jovyan

RUN pip install pipenv

COPY work /home/jovyan/work

RUN cd work && pipenv install --system --deploy