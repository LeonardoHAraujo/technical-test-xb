import React, { createContext, useEffect, useState } from 'react'
import { IAuthProvider, IContext, IUser } from './types'

import {
  loginRequest,
  setUserLocalStorage,
  getUserLocalStorage,
  registerRequest,
} from './util'

export const AuthContext = createContext<IContext>({} as IContext)

export const AuthProvider = ({ children }: IAuthProvider) => {
  const [user, setUser] = useState<IUser | null>()

  useEffect(() => {
    const user = getUserLocalStorage()
    user && setUser(user)
  }, [])

  async function authenticate(email: string, password: string) {
    const res = await loginRequest(email, password)
    const payload = { name: res.body.name, email, token: res.body.token }

    setUser(payload)
    setUserLocalStorage(payload)
  }

  async function register(name: string, email: string, password: string) {
    const res = await registerRequest(name, email, password)
    return res && true
  }

  function logout() {
    setUser(null)
    setUserLocalStorage(null)
  }

  return (
    <AuthContext.Provider value={{ ...user, authenticate, register, logout }}>
      {children}
    </AuthContext.Provider>
  )
}
