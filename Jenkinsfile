pipeline {
  agent any
  
  environment {
    DOCKER_IMAGE = 'khanhnq1301/seminar:latest'
    DEPLOY_USER = 'mlops'
    DEPLOY_HOST = '192.168.28.38'
  }
  stages {
    stage('Build Docker Image') {
      steps {
        
        script {
          docker_image = docker.build("${DOCKER_IMAGE}", "." )
          
        }
      }
    }

    stage('Push Docker Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-key', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
          sh 'echo $DOCKERHUB_PASS | docker login -u $DOCKERHUB_USER --password-stdin'
          script {
            docker_image.push()
          }
        }
      }
    }

    stage('Deploy') {
      steps {
        sshagent(['deploy-key']) {
          sh """
            ssh -o StrictHostKeyChecking=no ${DEPLOY_USER}@${DEPLOY_HOST} '
              docker pull ${DOCKER_IMAGE} &&
              docker stop app_container || true &&
              docker rm app_container || true &&
              docker run -d --name app_container -p 4001:4001 ${DOCKER_IMAGE}
            '
          """
        }
      }
    }
  }
}
