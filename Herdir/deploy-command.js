const { SlashCommandBuilder } = require('@discordjs/builders');
const { REST } = require('@discordjs/rest');
const { Routes } = require('discord-api-types/v9');
const { clientId, guildId, token } = require('./config.json');

const commands = [
	new SlashCommandBuilder()
		.setName('ping')
		.setDescription('Replies with pong!')
		.addStringOption(option => option.setName('input').setDescription('Enter a string'))
		.addIntegerOption(option => option.setName('int').setDescription('Enter an integer'))
		.addNumberOption(option => option.setName('num').setDescription('Enter a number'))
		.addBooleanOption(option => option.setName('choice').setDescription('Select a boolean'))
		.addUserOption(option => option.setName('target').setDescription('Select a user'))
		.addChannelOption(option => option.setName('destination').setDescription('Select a channel'))
		.addRoleOption(option => option.setName('muted').setDescription('Select a role'))
		.addMentionableOption(option => option.setName('mentionable').setDescription('Mention something')),
	new SlashCommandBuilder().setName('server').setDescription('Replies with server info!'),
	new SlashCommandBuilder().setName('user').setDescription('Replies with user info!'),
	new SlashCommandBuilder()
		.setName('echo')
		.setDescription('Replies with your input!')
		.addStringOption(option =>
			option.setName('input')
				.setDescription('The input to echo back')
				.setRequired(true)),
	new SlashCommandBuilder()
		.setName('gif')
		.setDescription('Sends a random gif!')
		.addStringOption(option =>
			option.setName('category')
				.setDescription('The gif category')
				.setRequired(true)
				.addChoice('Funny', 'gif_funny')
				.addChoice('Meme', 'gif_meme')
				.addChoice('Movie', 'gif_movie')),
	new SlashCommandBuilder()
		.setName('info')
		.setDescription('Get info about a user or a server!')
		.addSubcommand(subcommand =>
			subcommand
				.setName('user')
				.setDescription('Info about a user')
				.addUserOption(option => option.setName('target').setDescription('The user')))
		.addSubcommand(subcommand =>
			subcommand
				.setName('server')
				.setDescription('Info about the server')),
]
	.map(command => command.toJSON());

const rest = new REST({ version: '9' }).setToken(token);

rest.put(Routes.applicationGuildCommands(clientId, guildId), { body: commands })
	.then(() => console.log('Successfully registered application commands.'))
	.catch(console.error);
