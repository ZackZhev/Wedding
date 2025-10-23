# Wedding Invitation Website — Node.js/Express

Modern wedding invitation website with admin panel. Built with Node.js, Express, and EJS templating.

## Project Structure
```
Wedding/
├── server.js           # Express server
├── config.json         # Wedding configuration
├── package.json        # Node dependencies
├── Procfile           # Deployment config
├── views/             # EJS templates
│   ├── index.ejs      # Main invitation page
│   └── admin.ejs      # Admin panel
└── public/            # Static assets
    └── images/        # Images
        └── hero.jpg   # Hero image
```

## Installation & Running

### Development
```bash
npm install
npm start
```

### Development with Auto-Reload
```bash
npm install
npm run dev
```

The server will start on http://localhost:3000

- Main page: http://localhost:3000
- Admin panel: http://localhost:3000/admin

## Configuration

Edit the wedding details in two ways:

1. **Admin Panel**: Visit `/admin` to use the visual editor
   - After saving, click "Обновить превью" to see changes

2. **Manual**: Edit `config.json` directly

### Configuration Options

- **couple**: Bride and groom names
- **tagline**: Wedding invitation message
- **dateISO**: Wedding date/time in ISO format
- **address**: Wedding venue address
- **mapUrl**: Google Maps link
- **instagramUrl**: Instagram profile
- **whatsapp**: WhatsApp contact number
- **heroImage**: Path to hero image
- **gallery**: Array of gallery image URLs
- **music**: Background music settings
- **schedule**: Wedding program timeline
- **form**: RSVP form configuration

## Deployment

This project is configured for Heroku deployment with the included `Procfile`.

```bash
git push heroku main
```

## API Endpoints

- `GET /` - Main invitation page
- `GET /admin` - Admin panel
- `GET /api/config` - Get current configuration
- `PUT /api/config` - Update configuration

## Technology Stack

- **Backend**: Node.js with Express
- **Templating**: EJS
- **Styling**: Vanilla CSS with modern features
- **Frontend**: Vanilla JavaScript