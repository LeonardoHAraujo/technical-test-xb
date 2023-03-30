import React from 'react'
import { useNavigate } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import { Form, Input, Button, message } from 'antd'

import { SwitchTranslator } from '../SwitchTranslator'
import { useAuth } from '../../context/AuthProvider/useAuth'
import capivara from '../../assets/pappers/cavipara_papper.jpg'
import './styles.css'

export interface IForm {
  email: string
  password: string
}

export const Login = () => {
  const auth = useAuth()
  const navigate = useNavigate()
  const { t } = useTranslation()

  const onFinish = async ({ email, password }: IForm) => {
    try {
      await auth.authenticate(email, password)
      navigate('/')

    } catch(err) {
      message.error('Invalid email or password.')
    }
  }

  return (
    <div>
      <SwitchTranslator />
      <div className="login-page">
        <div className="login-box">
          <div className="illustration-wrapper">
            <img src={capivara} alt="Login"/>
          </div>
          <Form
            name="login-form"
            initialValues={{ remember: true }}
            onFinish={onFinish}
          >
            <p className="form-title">{t('titleLogin')}</p>
            <p>{t('subTitleLogin')}</p>
            <Form.Item
              name="email"
              rules={[{ required: true, message: `${t('validateEmailMessage')}` }]}
            >
              <Input
                placeholder="Email"
              />
            </Form.Item>

            <Form.Item
              name="password"
              rules={[{ required: true, message: `${t('validatePasswordMessage')}` }]}
            >
              <Input.Password
                placeholder={t('placeholderPassword') ?? 'Password'}
              />
            </Form.Item>

            <Form.Item>
              <Button type="primary" htmlType="submit" className="login-form-button">
                {t('btnLogin')}
              </Button>
            </Form.Item>
            <span>{t('or')} <a href="/register">{t('register')}</a></span>
          </Form>
        </div>
      </div>
    </div>
  )
}

