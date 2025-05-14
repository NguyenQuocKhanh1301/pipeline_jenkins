pipeline {
  agent any

  environment {
    DOCKER_IMAGE = 'khanhnq1301/seminar:latest'
    DEPLOY_USER = 'mlops'
    DEPLOY_HOST = '192.168.28.3'
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
        script {
          sshagent(['deploy-key']) {
            sh """
              ssh -o StrictHostKeyChecking=no ${DEPLOY_USER}@${DEPLOY_HOST} '
                docker stop app_container || true &&
                docker rm app_container || true &&
                docker rmi ${DOCKER_IMAGE} || true &&
                docker pull ${DOCKER_IMAGE} &&
                docker run -d --name app_container -p 8084:5006 ${DOCKER_IMAGE}
              '
            """
          }
        }
      }
    }
  }

  post {
    failure {
      emailext(
        subject: "❌ FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
        body: """<p>❌ Job <b>${env.JOB_NAME}</b> build #${env.BUILD_NUMBER} failed.</p>
                 <p><a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>""",
        to: 'khanh2003dakdoa@gmail.com'
      )
    }
  }
}
