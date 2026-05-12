<template>
  <view class="container" v-if="flower">
    <image class="detail-image" :src="flower.image" mode="widthFix" />

    <view class="detail-content">
      <view class="detail-header">
        <text class="flower-name">{{ flower.name }}</text>
        <text class="flower-price">¥{{ flower.price.toFixed(2) }}</text>
      </view>

      <view class="detail-category" v-if="flower.category">
        <text class="category-label">分类</text>
        <text class="category-value">{{ flower.category }}</text>
      </view>

      <view class="detail-desc">
        <text class="desc-label">描述</text>
        <text class="desc-text">{{ flower.description }}</text>
      </view>
    </view>
  </view>
  <view class="loading" v-else>
    <text>加载中...</text>
  </view>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { flowerApi, type Flower } from '@/common/api/flower'

const flower = ref<Flower | null>(null)

onMounted(async () => {
  const pages = getCurrentPages()
  const currentPage = pages[pages.length - 1] as any
  const id = currentPage.options?.id

  if (id) {
    try {
      flower.value = await flowerApi.getFlowerDetail(Number(id))
    } catch (error) {
      console.error('加载失败:', error)
      uni.showToast({ title: '加载失败', icon: 'none' })
    }
  }
})
</script>

<style scoped>
.container {
  min-height: 100vh;
  background-color: #fff;
}

.detail-image {
  width: 100%;
}

.detail-content {
  padding: 30rpx;
}

.detail-header {
  margin-bottom: 30rpx;
}

.flower-name {
  display: block;
  font-size: 40rpx;
  font-weight: bold;
  color: #333;
  margin-bottom: 15rpx;
}

.flower-price {
  display: block;
  font-size: 36rpx;
  color: #ff6b6b;
  font-weight: bold;
}

.detail-category {
  display: flex;
  align-items: center;
  padding: 20rpx 0;
  border-top: 1rpx solid #f0f0f0;
}

.category-label {
  font-size: 28rpx;
  color: #999;
  margin-right: 20rpx;
}

.category-value {
  font-size: 28rpx;
  color: #333;
}

.detail-desc {
  padding: 20rpx 0;
}

.desc-label {
  display: block;
  font-size: 28rpx;
  color: #999;
  margin-bottom: 15rpx;
}

.desc-text {
  display: block;
  font-size: 28rpx;
  color: #666;
  line-height: 1.6;
}

.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  color: #999;
}
</style>
