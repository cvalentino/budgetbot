tar -czvf python-files.tar.gz *.py
docker build -t budgetbot:latest .
rm python-files.tar.gz
# docker container run -d budgetbot