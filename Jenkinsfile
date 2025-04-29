// pipeline {
//     agent {
//         node{
//         label 'docker-agent-python'
//         }
//     }

//     environment {
//         VENV = "venv"
//     }
    
//     stages {
//         stage('Setup Environment') {
//             steps {
//                // cài đặt môi trường ảo
//                 sh 'python3 -m venv venv'
//                 sh 'venv/bin/pip install -r requirements.txt'
//             }
//         }
//         stage('Run Application') {
//             steps {
//                 sh 'nohup venv/bin/python ./jenkins/webdemo.py &'
//                 // Thêm delay để cho phép ứng dụng khởi động
//                 sh 'sleep 6'
//             }
//         }
//         stage('Test Application') {
//             steps {
//                 sh 'curl -s http://127.0.0.1:5004 | grep "i love ml"'
//             }
//         }
//     }
    
//     post {
//         always {
//             sh "pkill -f 'python3 ./jenkins/webdemo.py' || true"
//         }
//     }
// }

pipeline {
    agent {
        node {
            label 'docker-agent-python'
        }
    }

    environment {
        IMAGE_NAME = 'python:3.10'
    }

    stages {
        stage('Pull Docker Image and Run Flask App') {
            steps {
                script {
                    // Run a temporary container and execute Flask app
                    sh """
                        docker pull ${IMAGE_NAME}
                        docker run -d --name flask-app -p 5000:5000 \\
                            -v $(pwd):/app -w /app ${IMAGE_NAME} \\
                            /bin/bash -c "pip install -r requirements.txt && python app.py"
                    """
                }
            }
        }

        stage('Verify Container Running') {
            steps {
                sh 'docker ps'
            }
        }
    }

    post {
        always {
            echo "Cleaning up container..."
            sh "docker stop flask-app || true"
            sh "docker rm flask-app || true"
        }
    }
}
