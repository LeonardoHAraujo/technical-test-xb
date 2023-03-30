import React from 'react'
import 'antd/dist/reset.css'
import { BrowserRouter, Route, Routes } from 'react-router-dom'

import './App.css'
import { Login } from './components/Login'
import { Register } from './components/Register'
import { Home } from './components/Home'
import { AuthProvider } from './context/AuthProvider'
import { ProtectedLayout } from './components/ProtectedLayout'

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route
            path="/"
            element={
              <ProtectedLayout>
                <Home />
              </ProtectedLayout>
            }
          />

          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  )
}

export default App
