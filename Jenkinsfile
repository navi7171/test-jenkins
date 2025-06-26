pipeline {
// agent {
//	docker { image 'node:16-alpine' }
// }
 agent { label 'agent1' }

 environment {
    OPENSHIFT_API = 'https://api.r2wid4.ibm.aessatl.arrow.com:6443'
    NAMESPACE = 'main'
    SHELL_SCRIPT_PATH = 'packages.sh'
    PY_SCRIPT_PATH = 'openshift-deploy.py'
  }
 
 triggers {
     pollSCM('H/1 * * * *')  // Every 5 minutes
 }
	
   stages {

    stage('Cloning Git') {
	    steps{
	      sh 'echo checking out source code'
	    }  
     }  
 
    stage('SAST'){
      steps{
      	sh 'echo SAST stage'
	   }
    }

    
    stage('Build-and-Tag') {
    /* This builds the actual image; synonymous to
         * docker build on the command line */
      steps{	
        sh 'echo Build and Tag'
          }
    }

    stage('Post-to-dockerhub') {
     steps {
        sh 'echo post to dockerhub repo'
     }
    }

    stage('SECURITY-IMAGE-SCANNER'){
      steps {
        sh 'echo scan image for security'
     }
    }

    stage('Pull-image-server') {
      steps {
         sh 'echo pulling image ...'
       }
      }
    
    stage('DAST') {
      steps  {
         sh 'echo dast scan for security'
        }
    }

    stage('Login to OpenShift') {
      steps  {
         withCredentials([string(credentialsId: 'ocp-token', variable: 'OCP_TOKEN')]) {
          sh """
            oc login ${OPENSHIFT_API} --token=${OCP_TOKEN} --insecure-skip-tls-verify=true
            oc project ${NAMESPACE}
          """
        }
    }

    stage('Deploy to OpenShift') {
      steps  {
	    sh """
	        chmod +x ${SHELL_SCRIPT_PATH}
	        ${SHELL_SCRIPT_PATH}
            python ${PY_SCRIPT_PATH}
	    """
      }
    }
 }


}
