const BASE_URL = ''

export interface Flower {
  id: number
  name: string
  price: number
  image: string
  description: string
  category: string
  create_time: string
}

export interface FlowerListResponse {
  total: number
  items: Flower[]
}

export const flowerApi = {
  getFlowerList(offset: number = 0, limit: number = 10): Promise<FlowerListResponse> {
    return new Promise((resolve, reject) => {
      uni.request({
        url: `${BASE_URL}/api/flowers`,
        method: 'GET',
        data: { offset, limit },
        success: (res) => {
          if (res.statusCode === 200) {
            resolve(res.data as FlowerListResponse)
          } else {
            reject(new Error(`请求失败: ${res.statusCode}`))
          }
        },
        fail: (err) => {
          reject(err)
        }
      })
    })
  },

  getFlowerDetail(id: number): Promise<Flower> {
    return new Promise((resolve, reject) => {
      uni.request({
        url: `${BASE_URL}/api/flowers/${id}`,
        method: 'GET',
        success: (res) => {
          if (res.statusCode === 200) {
            resolve(res.data as Flower)
          } else {
            reject(new Error(`请求失败: ${res.statusCode}`))
          }
        },
        fail: (err) => {
          reject(err)
        }
      })
    })
  }
}
