import Vue from 'vue'

import 'normalize.css/normalize.css' // A modern alternative to CSS resets

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en' // lang i18n

import '@/styles/index.scss' // global css

import App from './App'
import store from './store'
import router from './router'

import '@/icons' // icon
import '@/permission' // permission control

// import axios from 'axios'

// import { getToken } from '@/utils/auth'

/**
 * If you don't want to use mock-server
 * you want to use MockJs for mock api
 * you can execute: mockXHR()
 *
 * Currently MockJs will be used in the production environment,
 * please remove it before going online ! ! !
 */
if (process.env.NODE_ENV === 'production') {
  const { mockXHR } = require('../mock')
  mockXHR()
}

// set ElementUI lang to EN
Vue.use(ElementUI, { locale })
// 如果想要中文版 element-ui，按如下方式声明
// Vue.use(ElementUI)

Vue.config.productionTip = false

// axios.interceptors.request.use((packet) => {
//     console.log('test')
//   var token = getToken()
//   if (token) {
//     packet.headers.Authorization = token
//   }
//   return packet
// }, (error) => {
//   if (error.response) {
//     return Promise.reject(error)
//   }
// })

// axios.interceptors.response.use(
//   res => {
//     // loadingInstance && loadingInstance.close();
//     // loading close...
//     console.log(res)
//     const status = res.status
//     if (status === 401) {
//       console.log('token expired')
//       window.location.reload()
//     } else {
//       return res
//     }
//   }
//   // error => {
//   //   // loading close...
//   //   // loadingInstance && loadingInstance.close();
//   //   if (error) {
//   //     // 请求配置发生的错误
//   //     if (!error.response) {
//   //       return console.log('Error', error.message);
//   //     }
//   //     // 获取状态码
//   //     const status = error.response.status;
//   //     // 提示错误信息
//   //     Vue.prototype.$message({
//   //       message: '错误',
//   //       type: "error"
//   //     });
//   //     // 错误状态处理
//   //     if (status === 401) {
//   //       router.push('/login')
//   //     } else if (status === 403) {
//   //       router.push('/login')
//   //     } else if (status >= 404 && status < 422) {
//   //       router.push('/404')
//   //     }
//   //   }
//   //   return Promise.reject(error);
//   // }
// )

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
