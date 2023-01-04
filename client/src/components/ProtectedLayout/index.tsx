import React from 'react'
import { Navigate } from 'react-router-dom'

import { IAuthProvider } from '../../context/AuthProvider/types'
import { getUserLocalStorage } from '../../context/AuthProvider/util'

export const ProtectedLayout = ({ children }: IAuthProvider) => {
  const user = getUserLocalStorage()
  return user ? children : <Navigate to="/login" />
}
