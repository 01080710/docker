FROM jupyter/base-notebook:python-3.10

USER root

# 安裝 golang
ENV GOLANG_VERSION=1.22.0
RUN wget https://dl.google.com/go/go${GOLANG_VERSION}.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go${GOLANG_VERSION}.linux-amd64.tar.gz && \
    rm go${GOLANG_VERSION}.linux-amd64.tar.gz

# 設定 Go 環境變數
ENV GOPATH=/home/jovyan/go
ENV PATH=$PATH:/usr/local/go/bin:$GOPATH/bin

# 安裝 gophernotes（Go kernel for Jupyter）
RUN apt-get update && \
    apt-get install -y git pkg-config build-essential && \
    chown -R jovyan:users /home/jovyan

USER jovyan

RUN go install github.com/gopherdata/gophernotes@latest && \
    mkdir -p /home/jovyan/.local/share/jupyter/kernels/gophernotes && \
    cp -r $GOPATH/pkg/mod/github.com/gopherdata/gophernotes@*/kernel/* /home/jovyan/.local/share/jupyter/kernels/gophernotes && \
    cp $GOPATH/bin/gophernotes /home/jovyan/.local/share/jupyter/kernels/gophernotes/

# 修正 kernel.json 指向絕對路徑
RUN sed -i "s|gophernotes|/home/jovyan/go/bin/gophernotes|g" /home/jovyan/.local/share/jupyter/kernels/gophernotes/kernel.json

# 啟動 JupyterLab（不需要 token）
CMD ["start-notebook.sh"]
#, "--NotebookApp.token=''"]