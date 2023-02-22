# syntax=docker/dockerfile:1

FROM python:3.10-slim
EXPOSE 8899

RUN mkdir -p /srv/tsn_af
WORKDIR /srv/tsn_af

COPY . .

RUN apt-get update && apt-get install -y gcc git
RUN pip install --no-cache-dir -r requirements.txt waitress
RUN pip install git+https://github.com/EVOLVED-5G/SDK-CLI.git@libraries

ENTRYPOINT ["waitress-serve"]
CMD [ "--listen=*:8899", "app:app" ]

