pipeline {
    agent {
        node{
        label 'docker-agent-python'
        }
    }

    environment {
        // Đường dẫn tới virtual environment
        VENV = "venv"
    }
    
    stages {
        stage('Setup Environment') {
            steps {
                // Tạo virtual environment và cài đặt Flask
                sh 'python3 -m venv venv'
                // sh 'venv/bin/pip install flask'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Application') {
            steps {
                sh 'nohup venv/bin/python ./jenkins/webdemo.py &'
                // Thêm delay để cho phép ứng dụng khởi động
                sh 'sleep 5'
            }
        }
        stage('Test Application') {
            steps {
                // Gửi yêu cầu HTTP và kiểm tra kết quả trả về có chứa "i love you"
                sh 'curl -s http://locallhost:5004 | grep "i love you"'
            }
        }
    }
    
    post {
        always {
            // Cleanup: Dừng các tiến trình Flask (nếu cần). Cách này rất đơn giản, bạn có thể cải tiến theo nhu cầu.
            sh "pkill -f 'python ./jenkins/webdemo.py' || true"
        }
    }
}
