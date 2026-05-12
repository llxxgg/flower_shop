<template>
  <view class="container">
    <view class="header">
      <text class="title">鲜花列表</text>
    </view>

    <view class="flower-grid">
      <view
        class="flower-card"
        v-for="flower in flowers"
        :key="flower.id"
        @click="goToDetail(flower.id)"
      >
        <image class="flower-image" :src="flower.image" mode="aspectFill" />
        <view class="flower-info">
          <text class="flower-name">{{ flower.name }}</text>
          <text class="flower-price">¥{{ flower.price.toFixed(2) }}</text>
        </view>
      </view>
    </view>

    <view class="loading-text" v-if="loading">
      <text>加载中...</text>
    </view>
    <view class="loading-text" v-if="noMore && flowers.length > 0">
      <text>没有更多了</text>
    </view>
    <view class="loading-text" v-if="!loading && flowers.length === 0">
      <text>暂无数据</text>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { flowerApi, type Flower } from '@/common/api/flower'

const flowers = ref<Flower[]>([])
const loading = ref(false)
const noMore = ref(false)
const offset = ref(0)
const limit = 10
const total = ref(0)

const loadData = async () => {
  if (loading.value || noMore.value) return

  loading.value = true
  try {
    const res = await flowerApi.getFlowerList(offset.value, limit)
    if (offset.value === 0) {
      flowers.value = res.items
    } else {
      flowers.value = [...flowers.value, ...res.items]
    }
    total.value = res.total
    if (flowers.value.length >= res.total) {
      noMore.value = true
    }
    offset.value += limit
  } catch (error) {
    console.error('加载失败:', error)
    uni.showToast({ title: '加载失败', icon: 'none' })
  } finally {
    loading.value = false
  }
}

const goToDetail = (id: number) => {
  uni.navigateTo({
    url: `/pages_flower/flower_detail/detail?id=${id}`
  })
}

onMounted(() => {
  loadData()
})
</script>

<style scoped>
.container {
  min-height: 100vh;
  background-color: #f5f5f5;
  padding: 20rpx;
}

.header {
  padding: 20rpx 0;
}

.title {
  font-size: 36rpx;
  font-weight: bold;
  color: #333;
}

.flower-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.flower-card {
  width: 48%;
  background-color: #fff;
  border-radius: 16rpx;
  margin-bottom: 20rpx;
  overflow: hidden;
  box-shadow: 0 2rpx 8rpx rgba(0, 0, 0, 0.1);
}

.flower-image {
  width: 100%;
  height: 320rpx;
}

.flower-info {
  padding: 20rpx;
}

.flower-name {
  display: block;
  font-size: 28rpx;
  color: #333;
  margin-bottom: 10rpx;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.flower-price {
  display: block;
  font-size: 32rpx;
  color: #ff6b6b;
  font-weight: bold;
}

.loading-text {
  text-align: center;
  padding: 30rpx;
  color: #999;
  font-size: 24rpx;
}
</style>
