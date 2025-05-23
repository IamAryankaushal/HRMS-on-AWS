// config values to be provided after AWS setup
const COGNITO_USER_POOL_ID = 'YOUR_USER_POOL_ID';
const COGNITO_CLIENT_ID = 'YOUR_CLIENT_ID';
const API_ENDPOINT = 'YOUR_API_GATEWAY_ENDPOINT';

// Initialize the Amazon Cognito credentials provider
AWS.config.region = 'YOUR_REGION'; // e.g : us-east-1

const userPool = new AmazonCognitoIdentity.CognitoUserPool({
  UserPoolId: COGNITO_USER_POOL_ID,
  ClientId: COGNITO_CLIENT_ID
});

// Current authenticated user
let currentUser = null;
let idToken = null;

// Check if user is already authenticated
function checkAuthentication() {
  const cognitoUser = userPool.getCurrentUser();
  
  if (cognitoUser != null) {
    cognitoUser.getSession((err, session) => {
      if (err) {
        console.error('Error getting session:', err);
        showLoginForm();
        return;
      }
      
      if (session.isValid()) {
        // Save the current user and token
        currentUser = cognitoUser;
        idToken = session.getIdToken().getJwtToken();
        
        // Get user attributes
        currentUser.getUserAttributes((err, attributes) => {
          if (err) {
            console.error('Error getting user attributes:', err);
            return;
          }
          
          // Find the name attribute
          const nameAttribute = attributes.find(attr => attr.Name === 'name');
          const emailAttribute = attributes.find(attr => attr.Name === 'email');
          
          if (nameAttribute) {
            document.getElementById('user-name').textContent = nameAttribute.Value;
          } else if (emailAttribute) {
            document.getElementById('user-name').textContent = emailAttribute.Value;
          }
        });
        
        // Show the main app
        document.getElementById('auth-section').classList.add('hidden');
        document.getElementById('main-section').classList.remove('hidden');
        
        // Initialize the app
        initializeApp();
      } else {
        showLoginForm();
      }
    });
  } else {
    showLoginForm();
  }
}

// Show the login form
function showLoginForm() {
  document.getElementById('auth-section').classList.remove('hidden');
  document.getElementById('main-section').classList.add('hidden');
}

// Handle login
function login(username, password) {
  const authenticationData = {
    Username: username,
    Password: password
  };
  
  const authenticationDetails = new AmazonCognitoIdentity.AuthenticationDetails(authenticationData);
  
  const userData = {
    Username: username,
    Pool: userPool
  };
  
  const cognitoUser = new AmazonCognitoIdentity.CognitoUser(userData);
  
  cognitoUser.authenticateUser(authenticationDetails, {
    onSuccess: function(result) {
      // Save the token and user
      idToken = result.getIdToken().getJwtToken();
      currentUser = cognitoUser;
      
      // Show the main app
      document.getElementById('auth-section').classList.add('hidden');
      document.getElementById('main-section').classList.remove('hidden');
      
      // Initialize the app
      initializeApp();
    },
    onFailure: function(err) {
      console.error('Authentication failed:', err);
      document.getElementById('auth-message').textContent = 'Authentication failed: ' + err.message;
    }
  });
}

// Handle logout
function logout() {
  if (currentUser) {
    currentUser.signOut();
    currentUser = null;
    idToken = null;
    
    // Show the login form
    showLoginForm();
  }
}

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
  // Login button
  document.getElementById('login-btn').addEventListener('click', () => {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    login(username, password);
  });
  
  // Logout button
  document.getElementById('logout-btn').addEventListener('click', logout);
  
  // Check if user is already authenticated
  checkAuthentication();
});