# Python + Next.js Full-Stack Application

A modern full-stack web application combining a **FastAPI backend** with a **Next.js frontend**, demonstrating API integration, CORS configuration, and TypeScript type safety.

## 📋 Project Overview

This project is a complete example of integrating a Python FastAPI backend with a Next.js React frontend. It includes:

- **Backend**: FastAPI server with REST API endpoints for user management
- **Frontend**: Next.js application with TypeScript and Tailwind CSS
- **Communication**: Client-side API calls from React to FastAPI with CORS enabled
- **Database**: In-memory user database with sample data

## 🗂️ Project Structure

```
.
├── main.py                          # FastAPI backend server
├── requirements.txt                 # Python dependencies
├── frontend/                        # Next.js frontend application
│   ├── app/
│   │   ├── globals.css             # Global styles
│   │   ├── layout.tsx              # Root layout component
│   │   └── page.tsx                # Home page (fetches users from API)
│   ├── public/                     # Static assets
│   ├── package.json                # Node.js dependencies and scripts
│   ├── next.config.ts              # Next.js configuration
│   ├── tsconfig.json               # TypeScript configuration
│   ├── eslint.config.mjs           # ESLint configuration
│   └── postcss.config.mjs          # PostCSS configuration
├── static/                          # Static files (legacy)
├── templates/                       # HTML templates
│   └── index.html
├── NEXTJS_SETUP.md                 # Setup guide
└── README.md                        # This file
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** installed on your system
- **Node.js 16+** and npm installed
- Git (optional)

### Installation

#### 1. Clone or Navigate to the Project

```bash
cd python-next.js
```

#### 2. Set Up the Backend

Install Python dependencies:

```bash
pip install -r requirements.txt
```

#### 3. Set Up the Frontend

Navigate to the frontend directory and install dependencies:

```bash
cd frontend
npm install
```

## 🎯 Running the Application

You'll need to run the backend and frontend in separate terminals.

### Terminal 1: Start FastAPI Backend

```bash
# From the root directory
python main.py
```

The backend will start on `http://localhost:8000`

**Available endpoints:**
- `GET /all-users` - Retrieve all users
- `GET /users/{user_id}` - Get a specific user by ID
- `GET /get-user?user_id=1` - Get user by query parameter
- `POST /submit` - Submit form data
- `GET /docs` - Interactive API documentation (Swagger UI)

### Terminal 2: Start Next.js Frontend

```bash
# From the frontend directory
npm run dev
```

The frontend will start on `http://localhost:3000`

Visit `http://localhost:3000` in your browser to see the application.

## 📦 Backend Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | 0.104.1 | Web framework |
| `uvicorn` | 0.24.0 | ASGI server |
| `pydantic` | 2.5.0 | Data validation |
| `python-multipart` | 0.0.6 | Form data handling |

## 🎨 Frontend Dependencies

### Runtime
- **Next.js** (16.1.1) - React framework
- **React** (19.2.3) - UI library
- **React DOM** (19.2.3) - React rendering

### Development
- **TypeScript** (^5) - Type safety
- **Tailwind CSS** (^4) - Utility-first CSS framework
- **ESLint** (^9) - Code linting
- **PostCSS** (^4) - CSS processing

## ✨ Key Features

✅ **CORS Configuration** - Frontend can communicate with backend seamlessly  
✅ **Type Safety** - Full TypeScript support in frontend  
✅ **REST API** - Clean RESTful endpoints  
✅ **Client-Side Data Fetching** - Dynamic data loading in React  
✅ **Responsive Design** - Tailwind CSS for styling  
✅ **API Documentation** - Swagger UI available at `/docs`  
✅ **Development Tools** - ESLint and TypeScript for code quality

## 🔧 Development Commands

### Backend
```bash
python main.py                      # Run the FastAPI server
```

### Frontend
```bash
npm run dev                         # Start development server
npm run build                       # Build for production
npm start                           # Start production server
npm run lint                        # Run ESLint
```

## 🌐 API Integration

The frontend fetches data from the backend's `/all-users` endpoint on the home page. The integration demonstrates:

- Setting up CORS in FastAPI
- Making fetch requests from React components
- Handling async data loading in Next.js
- Error handling and loading states

Example API call in React:
```typescript
const response = await fetch('http://localhost:8000/all-users');
const data = await response.json();
```

## 📝 Notes

- The backend includes an in-memory database with sample users
- CORS is configured to accept requests from `http://localhost:3000`
- The `/static` folder contains legacy static files and can be removed if not needed
- The `/templates` folder contains HTML templates (optional)

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [React Documentation](https://react.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)

## 📄 License

This project is open source and available under the MIT License.

## 💡 Tips

- Use the Swagger UI at `http://localhost:8000/docs` to test API endpoints
- Check the browser console for any CORS or network errors
- Ensure both servers are running for the full application to work
- The frontend will hot-reload when files are saved during development
