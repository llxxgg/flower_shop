<template>
  <view class="container">
    <view class="header">
      <text class="app-title">花店</text>
      <text class="app-subtitle">让生活充满花香</text>
    </view>
    <view class="entry-btn" @click="goToFlowerList">
      <text class="btn-text">进入花店</text>
    </view>
  </view>
</template>

<script setup lang="ts">
const goToFlowerList = () => {
  uni.navigateTo({
    url: '/pages_flower/flower_list/list'
  })
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #ff6b6b 0%, #ff8e8e 100%);
}

.header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 100rpx;
}

.app-title {
  font-size: 72rpx;
  font-weight: bold;
  color: #fff;
  margin-bottom: 20rpx;
}

.app-subtitle {
  font-size: 28rpx;
  color: rgba(255, 255, 255, 0.9);
}

.entry-btn {
  padding: 30rpx 80rpx;
  background-color: #fff;
  border-radius: 50rpx;
  box-shadow: 0 4rpx 20rpx rgba(0, 0, 0, 0.15);
}

.btn-text {
  font-size: 32rpx;
  color: #ff6b6b;
  font-weight: bold;
}
</style>
