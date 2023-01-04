import React, { useEffect, useState } from 'react'
import { Spin, Button } from 'antd'
import { useNavigate } from 'react-router-dom'
import { useTranslation } from 'react-i18next'

import {
  getUserLocalStorage,
  verifyTokenRequest
} from '../../context/AuthProvider/util'
import { SwitchTranslator } from '../SwitchTranslator'
import { useAuth } from '../../context/AuthProvider/useAuth'
import './styles.css'

const HomeView = () => {
  const auth = useAuth()
  const navigate = useNavigate()
  const { t } = useTranslation()

  const phrases = [
    'Se você puder jogar cavalo h5, jogue. ~ Lei de Davi Leandro.',
    'Chess speak for itself. ~ Hans Lima.',
    'Fala galerinha do xadrez, tudo beleza?',
    'Hans Lima.',
    'Magnu Carlu.',
    'Ricardinho Nakamura.',
    'Nesse momento senhoras e senhoras, nakamura, abandoooooona!!!'
  ]

  const [count, setCount] = useState<number>(0)
  const [phase, setPhase] = useState<string>(phrases[0])

  const randomPhase = () => {
    if (phrases[count] === undefined) {
      setCount(0)
      setPhase(phrases[1])

    } else {
      setCount(count + 1)
      setPhase(phrases[count])
    }
  }

  const logout = () => {
    auth.logout()
    navigate('/login')
  }

  return (
    <div>
      <SwitchTranslator />
      <div className="home-page">
        <div className="home-box">
          <div className="illustration-wrapper">
            <img src="https://preview.redd.it/ls3h501v74w31.jpg?width=640&crop=smart&auto=webp&s=6539c5fe90450f8602255b857381594db829bc63" alt="Login"/>
          </div>

          <div className="box-container">
            <div className="phrases-container">
              <h3>{phase}</h3>
            </div>
            <div className="buttons-container">
              <Button onClick={randomPhase} type="primary">{t('phase')}</Button>
              <Button onClick={logout} type="primary">{t('logout')}</Button>
            </div>
          </div>

        </div>
      </div>
    </div>
  )
}

export const Home = () => {
   /*
   *  Security layer for blocking localStorage
   *  manual manipulation.
  */

  const [isRender, setIsRender] = useState<boolean>(false)
  const navigate = useNavigate()

  const onLoad = async () => {
    const user = getUserLocalStorage()
    const isValidToken = await verifyTokenRequest(user.token)

    if (!isValidToken) {
      navigate('/login')
    }
  }

  useEffect(() => {
    onLoad()
      .then(() => setIsRender(true))
      .catch(err => console.log(err))
  }, [])

  return (
    <div>
      { isRender ? <HomeView /> : <Spin /> }
    </div>
  )
}

