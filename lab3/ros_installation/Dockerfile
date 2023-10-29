# TODO-PRM: 1a) ustaw obraz bazowy na odpowiednią wersję ros
FROM ...:...


RUN apt update && apt curl nano vim wget less lsb-release gnupg cmake make gcc g++ python3-pip

# TODO-PRM: 1a) dodaj komendę sourceującą skrypt setup ROSa do /root/.bashrc
RUN ...
RUN chmod +x /root/.bashrc

CMD [ "/bin/bash", "-c", "--", "while true; do sleep 20; done;" ]
