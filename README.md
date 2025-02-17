<h1>🗳️ Voting System Backend (Flask) & Frontend Integration</h1>

<h2>1️⃣ Run Your Flask Backend</h2>

<h3>(A) Activate Virtual Environment (If Using One)</h3>
<p>If you're using a virtual environment, activate it first.</p>

<b>For Windows (CMD/PowerShell):</b>
<pre><code>venv\Scripts\activate</code></pre>

<h3>(B) Install Dependencies (If Not Already Installed)</h3>
<p>Navigate to your project directory:</p>

<pre><code>cd "c:\...\backend"</code></pre>

<p>Then install required dependencies:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>(C) Set MongoDB Environment Variable</h3>
<p>Your error earlier was:</p>
<pre><code>MONGO_URI environment variable is not set!</code></pre>

<p>Make sure to set it before running the server.</p>

<b>For Windows (CMD):</b>
<pre><code>set MONGO_URI=mongodb+srv://yourusername:yourpassword@cluster.mongodb.net/</code></pre>

<b>For Windows (PowerShell):</b>
<pre><code>$env:MONGO_URI="mongodb+srv://yourusername:yourpassword@cluster.mongodb.net/"</code></pre>

<b>For Mac/Linux (Terminal):</b>
<pre><code>export MONGO_URI="mongodb+srv://yourusername:yourpassword@cluster.mongodb.net/"</code></pre>

<h3>(D) Run Flask Server</h3>
<p>Now, start your Flask API:</p>

<pre><code>python main.py</code></pre>
<p>or</p>
<pre><code>flask run --host=0.0.0.0 --port=5000</code></pre>

<p>You should see output like:</p>
<pre><code>* Running on http://127.0.0.1:5000/</code></pre>

<h2>2️⃣ Test API Endpoints</h2>
<p>Before integrating with the frontend, test your APIs using Postman or cURL.</p>

<h3>Register Voter (Face Registration)</h3>
<pre><code>curl -X POST http://127.0.0.1:5000/register -H "Content-Type: application/json" -d '{"voter_id": "12345"}'</code></pre>

<p>If successful, it should return:</p>
<pre><code>{
  "message": "Voter Registered Successfully!",
  "image_path": "backend/images/registered_faces/12345.jpg"
}</code></pre>

<h2>3️⃣ Connect Backend to Frontend</h2>

<h3>(A) Modify Frontend Code to Call API</h3>
<p>If your frontend is built with JavaScript (React, Vue, or Vanilla JS), use <code>fetch</code> or <code>axios</code>.</p>

<h3>(B) Example JavaScript Fetch Request</h3>
<p>Modify your frontend code to make a request to the Flask API.</p>

<pre><code>
function registerVoter() {
    let voterID = document.getElementById("voter_id").value;
    
    fetch("http://127.0.0.1:5000/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ voter_id: voterID })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        console.log("Image saved at: ", data.image_path);
    })
    .catch(error => console.error("Error:", error));
}
</code></pre>

<p>Call this function when a user submits the registration form.</p>

<h3>(C) Example HTML Form</h3>

```bash
<form onsubmit="event.preventDefault(); registerVoter();">
    <label>Enter Voter ID:</label>
    <input type="text" id="voter_id" required>
    <button type="submit">Register</button>
</form>
```

<h2>4️⃣ Run the Frontend</h2>

<p>If you're using a local HTML/CSS/JS frontend, just open <code>index.html</code>.</p>

<p>If you're using React or Vue, start the development server:</p>

<b>For React:</b>
<pre><code>npm start</code></pre>

<b>For Vue:</b>
<pre><code>npm run serve</code></pre>

<p>Now, test the voter registration from the frontend.</p>

<h2>🚀 Final Summary</h2>
<ul>
    <li>✅ 1️⃣ Run Flask backend (<code>python main.py</code>)</li>
    <li>✅ 2️⃣ Test API using Postman/cURL</li>
    <li>✅ 3️⃣ Modify frontend code to call API</li>
    <li>✅ 4️⃣ Start frontend and test registration</li>
</ul>

<p>🎯 Your voting system is now ready for deployment! 🚀</p>

</body>
</html>
