pipeline {
    agent {
        node{
        label 'docker-agent-python'
        }
    }

    environment {
        VENV = "venv"
    }
    
    stages {
        stage('Setup Environment') {
            steps {
               
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Application') {
            steps {
                sh 'nohup venv/bin/python ./jenkins/webdemo.py &'
                // Thêm delay để cho phép ứng dụng khởi động
                sh 'sleep 6'
            }
        }
        stage('Test Application') {
            steps {
                sh 'curl -s http://127.0.0.1:5004 | grep "i love ml"'
            }
        }
    }
    
    post {
        always {
            sh "pkill -f 'python3 ./jenkins/webdemo.py' || true"
        }
    }
}
