<template>
  <div>
    <div class="d-flex">
      <input 
        autofocus
        type="text"
        @input="onUserInput" 
        @keyup.enter="onSubmit"
        class="form-control"
      >
      <button 
        @click="onSubmit"
        class="btn btn-primary"
      >
        Add
      </button>
    </div>
    <div> {{ userInput.length }} / 50자</div>
  </div>
</template>

<script>

export default {
  name: 'Todoform',
  data() {
    return {
      userInput: '',
    }
  },
  methods: {
    onUserInput(e) {
      if (e.target.value.length > 50) {
        e.target.value = this.userInput
        return 
      }
      this.userInput = e.target.value
    },

    onSubmit() {
      // 검증 (문장 길이 제한)
      if (this.userInput.length > 50) {
        const errorMsg = '너무 길어요! 50자 이하로 써주세요!'
        this.$store.commit('UPDATE_ERROR', errorMsg)
        this.userInput=''
        return // 밑에 함수 실행되면 안되니깐 함수 끝내기!
      }

      this.$store.commit('UPDATE_ERROR', '')
      this.$store.commit('CREATE_TODO', this.newTodo(this.userInput))
      this.userInput='' // input 태그 초기화
    },

    newTodo(content) {
      return {
        id: this.$uuid.v1(),
        content,
        completed: false,
      }
    }
  }
}
</script>

<style>

</style>