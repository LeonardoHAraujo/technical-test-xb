import { Api } from '../../services/api'
import { IUser } from './types'

export function setUserLocalStorage(user: IUser | null) {
  localStorage.setItem('u', JSON.stringify(user))
}

export function getUserLocalStorage() {
  const json = localStorage.getItem('u')

  if (!json)
    return null

  return JSON.parse(json) ?? null
}

export async function verifyTokenRequest(token: string) {
  try {
    const req = await Api.get(`jwt/verify/${token}`)
    return req.data && true

  } catch (error) {
    return false
  }
}

export async function loginRequest(email: string, password: string) {
  try {
    const req = await Api.post('jwt/auth', { email, password })
    return req.data

  } catch (error) {
    return null
  }
}

export async function registerRequest(name: string, email: string, password: string) {
  try {
    const req = await Api.post('users/create', { name, email, password })
    return req.data

  } catch (error) {
    return null
  }
}

