<template>
  <div>
    <el-dialog
      title="Warning"
      :visible.sync="$store.state.reviewDialogVisible"
      width="90%"
      center>
      <span>It should be noted that the content will not be aligned in center by default</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="$store.state.reviewDialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="$store.state.reviewDialogVisible = false">Confirm</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
<<<<<<< HEAD
import axios from 'axios'
import Comment from '@/components/Community/Comments/Comment'


export default {
  name: 'ReviewDetail',
  components: {
    Comment,
  },
  computed: {
    review: function () {
      return this.$store.state.selectedReview
    }
  },
  methods: {
    deleteReview: function() {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/community/${this.$store.state.selectedMovie.id}/review/${this.review.id}/`,
        headers: this.$store.state.config,
      })
        .then(res => {
          console.log(res)
          this.$store.dispatch('getReviews')
          this.$store.state.reviewDialogVisible = false
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateReview: function() {
      axios({
        method: 'PUT',
        url: `http://127.0.0.1:8000/community/${this.$store.state.selectedMovie.id}/review/${this.review.id}/`,
        data: this.review,
        headers: this.$store.state.config,
      })
        .then(res => {
          console.log(res)
          this.$store.dispatch('selectReview', [this.$store.state.selectedMovie, this.review])
          this.$store.state.reviewDialogVisible = false
          this.$store.dispatch('selectMovie', this.$store.state.selectedMovie)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },

=======
export default {
  name: 'ReviewDetail',
>>>>>>> 2d52d823fde5494fbd9ae8272763de335c6c07f8
}
</script>

<style>

</style>