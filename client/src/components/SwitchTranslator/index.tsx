import React from 'react'
import { useTranslation } from 'react-i18next'

import en from '../../assets/icons/usa.png'
import br from '../../assets/icons/brazil.png'
import './style.css'

const langOptions = [
  {
    name: 'English',
    key: 'en',
    flag: en
  },
  {
    name: 'Portugues',
    key: 'ptBR',
    flag: br
  }
]

export const SwitchTranslator = () => {
  const { i18n } = useTranslation()

  return (
    <div className="switch-translator-container">
      {langOptions.map(lo => (
        <button style={{
          backgroundColor: i18n.language === lo.key ? 'lightgray' : '#f7f7f7'
        }}
          className="btn-translate"
          key={lo.key}
          onClick={() => i18n.changeLanguage(lo.key)}
        >
          <img className="img-translate" src={lo.flag} alt={lo.name}></img>
        </button>
      ))}
    </div>
  )
}
