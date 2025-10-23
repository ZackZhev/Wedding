const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

// Configuration
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());

const CONFIG_PATH = path.join(__dirname, 'config.json');

// Helper functions
function loadConfig() {
  const data = fs.readFileSync(CONFIG_PATH, 'utf-8');
  return JSON.parse(data);
}

function saveConfig(config) {
  fs.writeFileSync(CONFIG_PATH, JSON.stringify(config, null, 2), 'utf-8');
}

// Disable caching
app.use((req, res, next) => {
  res.set({
    'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
    'Pragma': 'no-cache',
    'Expires': '0'
  });
  next();
});

// Routes
app.get('/', (req, res) => {
  const config = loadConfig();
  res.render('index', { config });
});

app.get('/admin', (req, res) => {
  res.render('admin');
});

app.get('/api/config', (req, res) => {
  const config = loadConfig();
  res.json(config);
});

app.put('/api/config', (req, res) => {
  const config = req.body;
  saveConfig(config);
  res.json({ ok: true });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
