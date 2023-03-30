import React from 'react'
import { useNavigate } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import { Form, Input, Button, message } from 'antd'

import { SwitchTranslator } from '../SwitchTranslator'
import { useAuth } from '../../context/AuthProvider/useAuth'
import capivara from '../../assets/pappers/papper_capivara.jpg'
import './styles.css'

export interface IForm {
  name: string
  email: string
  password: string
}

export const Register = () => {
  const auth = useAuth()
  const navigate = useNavigate()
  const { t } = useTranslation()

  const onFinish = async ({ name, email, password }: IForm) => {
    try {
      const isRegistered = await auth.register(name, email, password)

      if (isRegistered) {
        navigate('/login')

      } else {
        message.error('User already exists.')
      }

    } catch(err) {
      message.error('Failed to register.')
    }
  }

  return (
    <div>
      <SwitchTranslator />
      <div className="register-page">
        <div className="register-box">
          <div className="illustration-wrapper">
            <img src={capivara} alt="Login"/>
          </div>
          <Form
            name="register-form"
            initialValues={{ remember: true }}
            onFinish={onFinish}
          >
            <p className="form-title">{t('register')}</p>
            <p>{t('subTitleRegister')}</p>

            <Form.Item
              name="name"
              rules={[{ required: true, message: `${t('validateNameMessage')}` }]}
            >
              <Input
                placeholder={t('placeholderName') ?? 'Name'}
              />
            </Form.Item>

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
              <Button type="primary" htmlType="submit" className="register-form-button">
                {t('btnRegister')}
              </Button>
            </Form.Item>
            <span>{t('or')} <a href="/login">{t('login')}</a></span>
          </Form>
        </div>
      </div>
    </div>
  )
}

