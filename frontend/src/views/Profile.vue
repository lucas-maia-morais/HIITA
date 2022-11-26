<template>
<div>
    <h2>Profile Page</h2>
<div>
    <p>Your account details are below:</p>
    <table>
        <tr>
            <td>Username:</td>
            <td>{{ account['username'] }}</td>
        </tr>
        <tr>
            <td>Password:</td>
            <td>{{ account['password'] }}</td>
        </tr>
        <tr>
            <td>Email:</td>
            <td>{{ account['email'] }}</td>
        </tr>
    </table>
</div>
</div>
</template>

<script>
export default {
  data() {
    return {
      account: {
        username: 'neymarjr',
        email: 'neymarjr@gmail.com',
        password: 'hexa',
      },
    };
  },
};
</script>
